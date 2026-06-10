with base as (
    select * from {{ref ('stg_air_quality')}}
),

city_summary as (
    select
        city,
        state,
        pollutant_id,
        round(avg(pollutant_avg), 2) as avg_pollution,
        round(min(pollutant_min), 2) as min_pollution,
        round(max(pollutant_max), 2) as max_pollution,
        count(*) as reading_count
    from base
    group by city, state, pollutant_id
)

select * from city_summary
order by avg_pollution 