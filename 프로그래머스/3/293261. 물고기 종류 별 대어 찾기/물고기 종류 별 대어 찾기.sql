-- 코드를 작성해주세요
select i.id, n.fish_name, i.length as LENGTH
from fish_info i
join fish_name_info n on i.fish_type = n.fish_type
where i.length = (
        select max(f.length)
        from fish_info f
        where f.fish_type = i.fish_type)
and i.length > 10
order by id asc