with base as (

    select * from {{ ref('stg_orders') }}

),

aggregated as (

    select
        customer_id,
        count(distinct invoice_id) as total_orders,
        sum(quantity) as total_items,
        sum(quantity * price) as total_revenue,
        min(invoice_date) as first_order_date,
        max(invoice_date) as last_order_date
    from base
    group by customer_id

)

select * from aggregated
