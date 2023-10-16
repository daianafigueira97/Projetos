-- Definição dos indicadores:
/*
1 - Total de vendas Internet por categoria;
2 - Receita total internet por mês do pedido;
3 - Receita e custo total internet por país;
4 - Total de vendas internet por sexo;
OBS. O ano considerado será 2013 (Ano de pedido)
*/
USE AdventureWorksDW2014
-- Definição de tabelas e suas (colunas):
/*
1 - FactInternetSales (SalesOrderNumber, OrderDate, OrderQuantity, TotalProductCost) = fis
2 - DimCustumer (FirstName + ' ' + LastName, Gender) = dc
3 - DimSalesTerritory (SalesTerritoryCountry) = dst
4 - DimProductCategory (EnglishProductCategoryName) = dpc
OBS. Na tabela 4 será necessário relacionamento em cadeia
*/

-- VIEW em sua definição se chamará: VENDAS_INTERNET
CREATE OR ALTER VIEW VENDAS_INTERNET 
AS
SELECT 
	fis.SalesOrderNumber AS 'Nº PEDIDO', 
	fis.OrderDate AS 'DATA PEDIDO', 
	dpc.EnglishProductCategoryName AS 'CATEGORIA PEDIDO',
	dc.FirstName + ' ' + LastName AS 'NOME CLIENTE', 
	dc.Gender AS 'GENERO',
	dst.SalesTerritoryCountry AS 'PAÍS',
	fis.OrderQuantity AS 'QTD. VENDIDA', 
	fis.TotalProductCost AS 'CUSTO DA VENDA',
	fis.SalesAmount AS 'RECEITA DA VENDA'
FROM FactInternetSales fis
INNER JOIN DimProduct dp ON fis.ProductKey = dp.ProductKey
	INNER JOIN DimProductSubcategory dps ON dp.ProductSubcategoryKey = dps.ProductSubcategoryKey
		INNER JOIN DimProductCategory dpc ON dps.ProductCategoryKey = dpc.ProductCategoryKey
INNER JOIN DimCustomer dc ON fis.CustomerKey = dc.CustomerKey
	INNER JOIN DimSalesTerritory dst ON fis.SalesTerritoryKey = dst.SalesTerritoryKey
WHERE
	YEAR(ORDERDATE) = 2013

