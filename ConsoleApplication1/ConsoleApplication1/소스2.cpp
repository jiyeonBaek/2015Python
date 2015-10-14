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
//Car::Car():price(1000),state('P'){// 인자없는 생성자
//	model = new char[strlen("SM5") + 1];
//	strcpy_s(model, strlen("SM5") + 1, "SM5");
//
//}
Car::Car() : price(1000), state('P'){// 인자없는 생성자
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
	cout << "모델 : " << model << endl;
	cout << "가격 : " << price << endl;
	cout << "상태 : " << state << endl;
	switch (state){
	case 'D':cout << "주행중" << endl;
		break;
	case 'P':cout << "주차중 " << endl;
		break;
	case 'N':cout << "기어중립" << endl;
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
	//SM5.ShowInfo();// "모델 : SM5 " "가격 : 1000" " 상태 : D"
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