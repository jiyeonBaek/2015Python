#include <iostream>
using namespace std;
class User{
protected:
	char* m_name;
	CellPhone& m_cell;
public:
	User(const char* name);
	void buy(const CellPhone* cell);
};
class CellPhone{
protected:
	char* m_pID;
	char* m_number;
public:
	CellPhone(const char* m_PID, const char* m_number);
	virtual ~CellPhone();
	virtual void show();
};
class SmartPhone:public CellPhone{
protected:
	char* m_networkIp;
public:
	SmartPhone(const char* pID, const char* number, const char* networkIp);
	~SmartPhone();
	void show();

};
CellPhone::CellPhone(const char* pID,const char* number){
	m_pID = new char[strlen(pID) + 1];
	strcpy(m_pID, pID);
	m_number = new char[strlen(number) + 1];
	strcpy(m_number, number);
}
CellPhone::~CellPhone(){
	delete[] m_pID;
	delete[] m_number;
}
void CellPhone::show(){
	cout << "고유번호 : " << m_pID << endl;
	cout << "전화번호 : " << m_number << endl;
}
SmartPhone::SmartPhone(const char* pID,const char* number, const char* networkIp)
	:CellPhone(m_pID,m_number)
{
	m_networkIp = new char[strlen(networkIp) + 1];
	strcpy(m_networkIp, networkIp);
}
SmartPhone::~SmartPhone(){
	delete[] m_networkIp;
}
void SmartPhone::show()
{
	cout << "고유번호 : " << m_pID << endl;
	cout << "전화번호 : " << m_number << endl;
	cout << "IP번호 : " << m_networkIp << endl;
}
User::User(const char* name){
	m_name = new char[strlen(name) + 1];
	strcpy(m_name, name);
}
void User::buy(const CellPhone* cell){
	m_cell = cell;
}

int main()
{
	CellPhone phone1("1234", "010-1111-1111");
	SmartPhone phone2("1234", "010-1111-2222", "127.0.0.1");
	User greenjoa("홍길동");
	greenjoa.buy(&phone1);
	greenjoa.buy(&phone2);
	return 0;
}