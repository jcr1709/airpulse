with source as (
    select * from read_csv_auto('C:/me/projects/airpulse/data/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69.csv', nullstr='NA')
),

renamed as (
    select
        country,
        city,
        state,
        station,
        last_update::timestamp as last_update,
        latitude::float as latitude,
        longitude::float as longitude,
        pollutant_id,
        pollutant_min::float as pollutant_min,
        pollutant_max::float as pollutant_max,
        pollutant_avg::float as pollutant_avg
    from source
    where pollutant_avg is not null    
)

select * from renamed