#include<iostream>

using namespace std;

class Car{
private:
	char* model;
	int price;
    char state;
	char c;
public:
	Car();
	Car(const char*_model, const int _price, const char _state);
	~Car();
	void ShowInfo();
	void setModel(const char* _model);
	void setState(const char _state){
		state = _state;
	}
};
//Car::Car():price(1000),state('P'){// ���ھ��� ������
//	model = new char[strlen("SM5") + 1];
//	strcpy_s(model, strlen("SM5") + 1, "SM5");
//
//}
Car::Car() : price(1000), state('P'){// ���ھ��� ������
	model = "SM5";

}

Car::Car(const char*_model, const int _price, const char _state) : price(_price),state(_state) {
	//model = new char[strlen(_model) + 1];
	//strcpy_s(model, strlen(_model) + 1, _model);
	 _model=&c;    
}
Car::~Car(){
	
	//delete[] model;
}
void Car::ShowInfo(){
	cout << "�� : " << model << endl;
	cout << "���� : " << price << endl;
	cout << "���� : " << state << endl;
	switch (state){
	case 'D':cout << "������" << endl;
		break;
	case 'P':cout << "������ " << endl;
		break;
	case 'N':cout << "����߸�" << endl;
		break;
	}

}
void Car::setModel(const char*_model){
	//if (model != NULL);
	//delete[]model;
	model = new char[strlen(_model) + 1];
	strcpy_s(model, strlen(_model) + 1, _model);
}


int main(){

	//Car SM5;
	//SM5.ShowInfo();// "�� : SM5 " "���� : 1000" " ���� : D"
	//cout << endl << endl;
	//SM5.setModel("EQUSS");
	//SM5.setState('D');
	//SM5.ShowInfo();
	//cout << endl << endl;
	//Car QM5("QM5", 2000, 'P');
	//QM5.setState('D');
	//QM5.ShowInfo();
	
	Car car[5];
	//car[0].setModel("BMW");
	//car[2].setModel("Benz");
	//car[1].setModel("Bid");
	car[0].ShowInfo();
	car[1].ShowInfo();
	car[2].ShowInfo();
	return 0;
}