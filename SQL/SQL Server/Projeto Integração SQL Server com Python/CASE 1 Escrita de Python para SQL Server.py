{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cf296ba6-3519-46fe-b861-b88ade013f88",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pyodbc in c:\\users\\daiana figueira\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (5.0.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pyodbc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ec5ea403-ff1e-4f04-90d2-593f8ada5af7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pyodbc in c:\\users\\daiana figueira\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (5.0.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pyodbc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "f0e888cd-c2d9-4000-aae3-d936ff693923",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Conexão bem sucedida\n"
     ]
    }
   ],
   "source": [
    "import pyodbc\n",
    "dados_conexao = (\n",
    "    \"Driver = {ODBC Driver 18 for SQL Server};\"\n",
    "    \"Server = 192.168.3.17;\"\n",
    "    \"Database = PythonSQL;\"\n",
    ")\n",
    "SERVER = '192.168.3.17'\n",
    "DATABASE = 'PythonSQL'\n",
    "USERNAME = 'daiana.figueira'\n",
    "PASSWORD = '141218Dm'\n",
    "\n",
    "connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes'\n",
    "\n",
    "conn = pyodbc.connect(connectionString)\n",
    "print(\"Conexão bem sucedida\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "b357ee59-5ab5-41e5-a685-b0d1d9e75849",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Conexão bem sucedida\n"
     ]
    }
   ],
   "source": [
    "import pyodbc\n",
    "dados_conexao = (\n",
    "    \"Driver = {ODBC Driver 18 for SQL Server};\"\n",
    "    \"Server = 192.168.3.17;\"\n",
    "    \"Database = PythonSQL;\"\n",
    ")\n",
    "SERVER = '192.168.3.17'\n",
    "DATABASE = 'PythonSQL'\n",
    "USERNAME = 'daiana.figueira'\n",
    "PASSWORD = '141218Dm'\n",
    "\n",
    "connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes'\n",
    "\n",
    "conn = pyodbc.connect(connectionString)\n",
    "print(\"Conexão bem sucedida\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "13de29ee-0857-4457-b8ae-9d2fa038f40f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Conexão bem sucedida\n"
     ]
    }
   ],
   "source": [
    "import pyodbc\n",
    "dados_conexao = (\n",
    "    \"Driver = {ODBC Driver 18 for SQL Server};\"\n",
    "    \"Server = 192.168.3.17;\"\n",
    "    \"Database = PythonSQL;\"\n",
    ")\n",
    "SERVER = '192.168.3.17'\n",
    "DATABASE = 'PythonSQL'\n",
    "USERNAME = 'daiana.figueira'\n",
    "PASSWORD = '141218Dm'\n",
    "\n",
    "connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes'\n",
    "\n",
    "conexao = pyodbc.connect(connectionString)\n",
    "print(\"Conexão bem sucedida\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "de87ab71-19fb-46c9-a17e-004d6bb306c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "cursor = conexao.cursor()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "608eeee2-d0c6-4149-8967-e6ee0756baea",
   "metadata": {},
   "outputs": [],
   "source": [
    "comando = \"\"\" \n",
    "INSERT INTO Vendas(id_venda, data_venda, cliente, produto, preco, quantidade)\n",
    "VALUES\n",
    "\t(1, '22/04/2022', 'Ana', 'Celular', 2000, 1) \"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2a8710cc-6768-453e-8344-8b1a16c1987f",
   "metadata": {},
   "outputs": [],
   "source": [
    "cursor.execute(comando)\n",
    "cursor.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ea7d63af-2d78-4104-acd9-45728451c4b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "cursor = conexao.cursor()\n",
    "id = 5\n",
    "data = \"17/06/2022\"\n",
    "cliente = \"Erica\"\n",
    "produto = \"Celular\"\n",
    "preco = 1500\n",
    "quantidade = 1\n",
    "comando = f\"\"\" \n",
    "INSERT INTO Vendas(id_venda, data_venda, cliente, produto, preco, quantidade)\n",
    "VALUES\n",
    "\t({id}, '{data}', '{cliente}', '{produto}', {preco}, {quantidade}) \"\"\"\n",
    "cursor.execute(comando)\n",
    "cursor.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c793710-0fd4-436e-a9d4-60cbb77839ed",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
