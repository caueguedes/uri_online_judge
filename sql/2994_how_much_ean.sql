SELECT
    worked_hours.name,
    ROUND(SUM(worked_hours.salary),1) as salary
FROM (
    SELECT
        doctors.name,
        ((attendances.hours * 150) * (1+ work_shifts.bonus/100)) as salary
	FROM attendances JOIN doctors        ON attendances.id_doctor = doctors.id
                    JOIN work_shifts    ON attendances.id_work_shift = work_shifts.id

) as worked_hours
GROUP BY worked_hours.name
ORDER BY salary DESC
