//#include<iostream>
//#include<cstring>
//using namespace std;
//class Car{
//private:
//	char* model;
//	int price;
//	char mode;
//public:
//	friend void ShowDrivingCar(Car *car);
//	Car();
//	Car(const char*_model, const int &price); //함수 안에서 이거 안바꿀꺼야  그러나 사용할떄 인자로 넘길때는 상관없어용;  void 함수() const 는 함수내에서 변경없다.
//	Car(const Car& car);
//	~Car();
//	void Show() const;
//	void setModel(const char* model);// 아래와 동일
//	void setMode(const char& mode);// 함수 내에서 mode를 참고만 하겠다.
//	void move()const;
//	Car getCar(){ return *this; }
//};
//Car::Car() :price(1000), mode('P'){ //디폴트
//	model = new char[strlen("SM5") + 1];
//	strcpy_s(model, strlen("SM5") + 1, "SM5");
//}
//Car::Car(const char* _model, const int& _price)//인자 있는 생성자
//	: price(_price), mode('P')
//{
//	model = new char[strlen(_model) + 1];
//	strcpy_s(model, strlen(_model) + 1, _model);
//		
//}
//Car::Car(const Car& car){// 깊은 복사생성자
//	cout << "복사생성자" << endl;
//	model = new char[strlen(car.model) + 1];
//	strcpy_s(model, strlen(car.model) + 1, car.model);
//	price = car.price;
//	mode = car.mode;
//}
//void Car::Show() const{
//	cout << "Model : " << model;
//	cout << "Price : " << price;
//	cout << "Mode : " << mode << endl;
//}
//Car::~Car(){
//	delete[] model;
//}
//void Car::setModel(const char* _model){
//	if (model != NULL)
//		delete[] model;
//	this->model = new char[strlen(_model) + 1];
//	strcpy_s(model, strlen(_model) + 1, _model);
//}
//void Car::setMode(const char& mode){
//	this->mode = mode;
//}
//void Car::move()const {
//	switch (mode){
//	case 'P':
//		cout << "주차 " << endl;
//		break;
//	case 'D':
//		cout << "주행" << endl;
//
//		break;
//	case 'R':
//		cout << "후진" << endl;
//		break;
//	case 'N':
//		cout << "중립" << endl;
//		break;
//	}
//}
//void ShowDrivingCar( Car *car){
//	for (int i = 0; i < 5; i++){
//		if (car[i].mode == 'D')
//			 car[i].Show();
//	}
//}
//
//int main(){
//	cout << "201110932 구건모" << endl;
//	Car carArr[5];
//	int a=3;
//	carArr[0].setMode('D');
//	carArr[0].setModel("Tico");
//	carArr[2].setMode('D');
//	carArr[4].setMode('D');
//	carArr[4].setModel("k9");
//	ShowDrivingCar(carArr);
//	return 0;
//}