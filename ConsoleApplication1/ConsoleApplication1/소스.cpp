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
//	Car(const char*_model, const int &price); //�Լ� �ȿ��� �̰� �ȹٲܲ���  �׷��� ����ҋ� ���ڷ� �ѱ涧�� ��������;  void �Լ�() const �� �Լ������� �������.
//	Car(const Car& car);
//	~Car();
//	void Show() const;
//	void setModel(const char* model);// �Ʒ��� ����
//	void setMode(const char& mode);// �Լ� ������ mode�� ���� �ϰڴ�.
//	void move()const;
//	Car getCar(){ return *this; }
//};
//Car::Car() :price(1000), mode('P'){ //����Ʈ
//	model = new char[strlen("SM5") + 1];
//	strcpy_s(model, strlen("SM5") + 1, "SM5");
//}
//Car::Car(const char* _model, const int& _price)//���� �ִ� ������
//	: price(_price), mode('P')
//{
//	model = new char[strlen(_model) + 1];
//	strcpy_s(model, strlen(_model) + 1, _model);
//		
//}
//Car::Car(const Car& car){// ���� ���������
//	cout << "���������" << endl;
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
//		cout << "���� " << endl;
//		break;
//	case 'D':
//		cout << "����" << endl;
//
//		break;
//	case 'R':
//		cout << "����" << endl;
//		break;
//	case 'N':
//		cout << "�߸�" << endl;
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
//	cout << "201110932 ���Ǹ�" << endl;
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