//#include<iostream>
//
//using namespace std;
//class Account{
//private:
//	char * m_accNum;
//	int m_balance;
//	static int m_count;
//public:
//	
//	Account();
//	Account(const char* accNum, const int &balance);//int& balance =1000 �̰Ǿȵ� �ֳİ�? ���۷����� �����ε� ������ٰ� ���� ���̴°� ���̾ȵ��ݾ�? ���ϼ������� ������ �����ϴٴ� �Ҹ���???
//	Account(const Account& acc);
//	~Account();
//	void show();
//	void deposit(const int& money);
//	void withdraw(const int&money);
//	static void showCount();//static �Լ������� static ����� ȣ���Ҽ� �ֽ��ϴ� �ֳ��ϸ� � ��ü�� �ɹ������� �ҷ� ������ �˼������ �����Ϸ���..
//};
//int Account::m_count = 0;
//void Account::showCount(){
//	cout << "���� �輳�� ������ �� : " << m_count<<endl;
//}
//Account::Account():m_balance(0){
//	m_accNum = new char[strlen("000-0000-0000") + 1];
//	strcpy_s(m_accNum, strlen("000-0000-0000") + 1, "000-0000-0000");
//	m_count++;
//}
//Account::Account(const char* accNum, const int &balance):m_balance(balance){
//	m_accNum = new char[strlen(accNum) + 1];
//	strcpy_s(m_accNum, strlen(accNum) + 1,accNum);
//	m_count++;
//}
//Account::~Account(){
//	delete[] m_accNum;
//	m_count--;
//}
//Account::Account(const Account& acc){
//	m_accNum = new char[strlen(acc.m_accNum) + 1];
//	strcpy_s(m_accNum, strlen(acc.m_accNum) + 1, acc.m_accNum);
//	m_balance = acc.m_balance;
//	m_count++;
//}
//void Account::show(){
//	cout << "���¹�ȣ : " << m_accNum << endl;
//	cout << "��    �� : " << m_balance << endl;
//}
//void Account::deposit(const int& money){
//	m_balance += money;
//	cout << "�Ա��� �ܾ� : " << m_balance<<endl;
//}
//void Account::withdraw(const int&money){
//	if (m_balance >=money){
//		m_balance -= money;
//		cout << "����� �ܾ� : " << m_balance<<endl;
//	}
//	else{
//		cout << "�ܾ��̺����մϴ�, ���� �ܾ� : " << m_balance << endl;
//	}
//}
//int main(){
//
//	cout << "201110932 ���Ǹ� " << endl;
//
//	Account acc1;
//	Account acc2("813601-079832",5000);
//	acc1.deposit(1000);
//	acc2.show();
//	acc1.show();
//	Account acc3(acc2);
//	acc3.show();
//	acc1.withdraw(7000);
//	acc1.withdraw(3000);
//	Account::showCount();
//	acc1.showCount();
//	return 0;
//}