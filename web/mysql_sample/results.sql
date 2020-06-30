use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
select name from store

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale;

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select DISTINCT s.store_id from store s
inner join sale as ss
on ss.store_id = s.store_id;


-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select DISTINCT store.store_id from store
left join sale 
on store.store_id = sale.store_id
where sale.store_id is NULL;

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select  product.name, avg(sale.total / sale.quantity) from product
inner join sale
on product.product_id = sale.product_id 
GROUP BY product.name 
ORDER BY product.product_id

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select  product.name  from product
join sale
on product.product_id = sale.product_id 
ORDER BY product.name limit 1

-- 8. Получить названия всех складов, с которых продавался только один продукт
select ...

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select ...

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select ...
