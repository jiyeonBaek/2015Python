#include<iostream>
#include<Windows.h>
#include<conio.h>
#include<iomanip>
using namespace std;

class Product{
private:
	int m_pId;
	char* m_pName;
	int m_pStock;
public:
	Product();
	Product(const int &pId, const char* pName, const int &pStock);
	Product(const Product& prod);
	~Product();
	int getId();
	void addStock(const int& stock);
	void show();
	int getStock(){
		return m_pStock;
	}
};
	Product::Product() :m_pId(0), m_pStock(0){
		m_pName = new char[strlen("noinfo") + 1];
		strcpy_s(m_pName, strlen("noinfo") + 1, "noinfo");
	}
	Product::~Product(){
		delete[] m_pName;
	}
	Product::Product(const int &pId, const char* pName, const int &pStock) :m_pId(pId), m_pStock(pStock){
		m_pName = new char[strlen(pName) + 1];
		strcpy_s(m_pName, strlen(pName) + 1, pName);
	}
	Product::Product(const Product& prod) : m_pId(prod.m_pId), m_pStock(prod.m_pStock){
		m_pName = new char[strlen(prod.m_pName) + 1];
		strcpy_s(m_pName, strlen(prod.m_pName) + 1, prod.m_pName);
	}
	int Product::getId(){
		return m_pId;
	}
	void Product::addStock(const int& stock){
		m_pStock += stock;
	}
	void Product::show(){
		cout << setw(3) << setfill('0') << m_pId;
		cout << "\t" << m_pName << "\t" << m_pStock << endl;
	}
	int menu(){
		system("cls");
		int num;
		cout << "1) ��ǰ�԰� 2)��ǰ��Ȳ 3)���� 4) ���� " << endl;
		cout << "�۾��� ��ȣ�� �����ϼ���: ";
		cin >> num;
		if (num >= 1 && num <= 3){ return num; }
		else{
			cout << "��ȣ�� �� �� �Է��ϼ̽��ϴ�." << endl;
			_getch();
			return menu();
		}
	}

	void registerProduct(Product**(&data), const int& pCount, int& cCount){
		system("cls");
		cout << "��ǰ �԰� ȭ��" << endl;
		int id, stock;
		char name[10];
		cout << "��ǰ�ڵ带 �Է��ϼ��� : ";
		cin >> id;
		for (int i = 0; i < cCount; i++){
			if (data[i]->getId() == id){
				cout << "�԰���� : ";
				cin >> stock;
				data[i]->addStock(stock);
				cout << "�԰� ���������� �Ϸ�Ǿ����ϴ�." << endl;
				_getch();
				return;
			}
		}
		if (cCount < pCount){
			cout << " ��ǰ �̸� : ";
			cin >> name;
			cout << "�԰� ���� :";
			cin >> stock;
			data[cCount++] = new Product(id, name, stock);
			cout << "�԰� �Ϸ�Ǿ����ϴ�." << endl;
			_getch();
			return;

		}
		else{
			cout << "���̻� ���ο� �߰� �԰�� �Ұ��մϴ�." << endl;
			_getch();
			return;
		}

	}
	void showProduct(Product**(&data), int &cCount){
		system("cls");
		cout << "*********************��ǰ ��Ȳ*********************" << endl;
		cout << "***************************************************" << endl;

		for (int i = 0; i < cCount; i++)
			data[i]->show();
		cout << "***************************************************" << endl;
		_getch();
	}
	void sortProduct(Product**(&data), int &cCount){
		Product ** pdata = new Product*[cCount];
		for (int i = 0; i < cCount; i++){
			pdata[i] = data[i];
		}
		for (int i = 0; i < cCount - 1; i++){
			for (int j = i + 1; j < cCount; j++){
				if (pdata[i]->getStock() < pdata[j]->getStock()){
					Product *temp;
					temp = pdata[i];
					pdata[i] = pdata[j];
					pdata[j] = temp;
				}
			}
		}
		for (int i = 0; i < cCount; i++)
			pdata[i]->show();
		_getch();
	
		delete[] pdata;
	}

	int main(){
		cout << "201110932 ���Ǹ�" << endl << endl << endl;

		int pCount, cCount = 0;
		cout << "��� ��ǰ�� �Ǹ��ұ�� :";
		cin >> pCount;
		Product** data = new Product*[pCount];
		if (data != NULL){
			cout << "���������� �����Ǿ����ϴ�." << endl;
			_getch();

			while (1){
				switch (menu()){
				case 1:
					registerProduct(data, pCount, cCount);
					break;
				case 2:
					showProduct(data, cCount);
					break;
				case 3:
					sortProduct(data, cCount);
					break;
				case 4:
					cout << "�ý����� �����մϴ�." << endl;
					for (int i = 0; i < cCount; i++){
						delete data[i];
					}
					delete data;
					_getch();
					return 0;
					
				}
			}
		}
		else
			cout << "��ǰ ������ ���� �ʾҽ��ϴ�." << endl;

		return 0;
	}
