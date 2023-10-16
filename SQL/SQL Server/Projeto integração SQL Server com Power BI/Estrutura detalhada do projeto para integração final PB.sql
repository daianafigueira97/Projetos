-- Definição dos indicadores:

/*
GUIA GERAL
1 - Receita total;
2 - Quantidade vendida;
3 - Total de categoria de produtos;
4 - Quantidade de clientes;
5 - Receita total e lucro total por mês;
6 - Margem de Lucro;
7 - Quantidade vendida por mês;
8 - Lucro por país;
*/

/*
GUIA CLIENTES
1 - Vendas por país;
2 - Clientes por país;
3 - Vendas por gênero;
4 - Vendas por categoria;
*/

-- Definição das tabelas e suas (colunas):

/*
1 - FactInternetSales (SalesOrderNumber, OrderDate, OrderQuantity, SalesAmount, TotalProductCost) = fis
2 - DimProductcategory (EnglishProductCategoryName) = dpc
3 - DimCustomer (CustomerKey, FirstName + ' ' + LastName, Gender) = dc
4 - DimGeography (EnglishCountryRegionName) = dg
*** Coluna adicional a ser calculada: SalesAmount - TotalProductCost = (Lucro)
OBS. tabela 2 será necessário relacionamento em cadeia.
*/

-- Nome definido para VIEW COMERCIAL_ADW

USE AdventureWorksDW2014


CREATE OR ALTER VIEW COMERCIAL_ADW
AS		
SELECT
	fis.SalesOrderNumber AS 'Nº DO PEDIDO', 
	fis.OrderDate AS 'DATA PEDIDO', 
	fis.OrderQuantity AS 'QTD, VENDIDA', 
	fis.SalesAmount AS 'RECEITA VENDA', 
	fis.TotalProductCost AS 'CUSTO VENDA',
	dpc.EnglishProductCategoryName AS 'CATEGORIA PRODUTO',
	dc.CustomerKey AS 'ID CLIENTE', 
	dc.FirstName + ' ' + dc.LastName AS 'NOME CLIENTE', 
	REPLACE(REPLACE(dc.Gender, 'M', 'Masculino'), 'F', 'Feminino') AS 'GENERO',
	dg.EnglishCountryRegionName AS 'PAÍS',
	fis.SalesAmount - fis.TotalProductCost AS 'LUCRO VENDA'
FROM FactInternetSales fis
INNER JOIN DimProduct dp ON fis.ProductKey = dp.ProductKey
	INNER JOIN DimProductSubcategory dps ON dp.ProductSubcategoryKey = dps.ProductSubcategoryKey
		INNER JOIN DimProductCategory dpc ON dps.ProductCategoryKey = dpc.ProductCategoryKey
INNER JOIN DimGeography dg ON fis.SalesTerritoryKey = dg.SalesTerritoryKey
	INNER JOIN DimCustomer dc ON fis.CustomerKey = dc.CustomerKey
