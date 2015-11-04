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
//	Account(const char* accNum, const int &balance);//int& balance =1000 이건안됨 왜냐고? 레퍼런스가 별명인데 상수에다가 별명 붙이는게 말이안되잖아? 붙일수있으면 변경이 가능하다는 소린데???
//	Account(const Account& acc);
//	~Account();
//	void show();
//	void deposit(const int& money);
//	void withdraw(const int&money);
//	static void showCount();//static 함수에서는 static 멤버만 호출할수 있습니다 왜냐하면 어떤 객체의 맴버변수를 불러 오는지 알수없어요 컴파일러가..
//};
//int Account::m_count = 0;
//void Account::showCount(){
//	cout << "현재 계설된 계좌의 수 : " << m_count<<endl;
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
//	cout << "계좌번호 : " << m_accNum << endl;
//	cout << "잔    액 : " << m_balance << endl;
//}
//void Account::deposit(const int& money){
//	m_balance += money;
//	cout << "입금후 잔액 : " << m_balance<<endl;
//}
//void Account::withdraw(const int&money){
//	if (m_balance >=money){
//		m_balance -= money;
//		cout << "출금후 잔액 : " << m_balance<<endl;
//	}
//	else{
//		cout << "잔액이부족합니다, 현재 잔액 : " << m_balance << endl;
//	}
//}
//int main(){
//
//	cout << "201110932 구건모 " << endl;
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