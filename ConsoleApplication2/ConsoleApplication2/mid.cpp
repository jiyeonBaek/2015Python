#include<iostream>

using namespace std;
class Air{
private:
	char* m_dest;
	char* m_depart;
	int m_row;
	int m_col;
	bool** m_seat;

public:
	Air();
	Air(char*dest, char*depart,  int row, int col);
	Air(const Air&);
	~Air();
	void show();
};
void Air::show(){
	int left_seat = 0;

	for (int i = 0; i < m_row; i++){
		for (int j = 0; j < m_col; j++){
			left_seat += m_seat[i][j];
		}
	}
	cout << m_dest << "  " <<m_depart << "  " << left_seat;
}
Air::Air():m_row(10),m_col(10){
	m_dest = new char[strlen("목적지") + 1];
	strcpy_s(m_dest, strlen("목적지") + 1, "목적지");
	m_depart = new char[strlen("출발지") + 1];
	strcpy_s(m_depart, strlen("출발지") + 1, "출발지");
	m_seat = new bool*[m_row];
	for (int i = 0; i < m_row; i++){
		m_seat[i] = new bool[m_col];
	}
	for (int i = 0; i < m_row; i++){
		for (int j = 0; j < m_col; j++){
			m_seat[i][j] = 1;
		}
	}
}
Air::Air(char*depart, char*dest, int row, int col){
	m_dest = new char[strlen(dest) + 1];
	strcpy_s(m_dest, strlen(dest) + 1, dest);
	m_depart = new char[strlen(depart) + 1];
	strcpy_s(m_depart, strlen(depart) + 1, depart);
	m_row = row;
	m_col = col;
	m_seat = new bool*[m_row];
	for (int i = 0; i < m_row; i++){
		m_seat[i] = new bool[m_col];
	}
	for (int i = 0; i < m_row; i++){
		for (int j = 0; j < m_col; j++){
			m_seat[i][j] = 1;
		}
	}
}
Air::~Air(){
	delete[] m_dest;
	delete[] m_depart;
	for (int i = 0; i < m_col; i++)
		delete[] m_seat[i];
	delete[] m_seat;
}
int menu(){
	cout << "==============Koo AirLine===============" << endl;
	cout << "1) 운항추가 2)운항조회 3)항공예약 4)종료" << endl;
	int sel;
	cin >> sel;
	if (0 < sel&&sel < 5){
		return sel;
	}
	else  return menu();
}
void addAir(Air ** air,int& pCount){
	if (pCount < 5){
		cout << "출발지를 입력하세요 : ";
		char depart[10];
		cin >> depart;
		cout << "목적지를 입력하세요 : ";
		char dest[10];
		cin >> dest;
		int row, col;
		cout << "행과 열을 입력하세요 : ";
		cin >> row >> col;

		if (dest == depart){
			addAir(air, pCount);
		}
		else{
			air[pCount++] = new Air(depart, dest, row, col);
		}
	}
	else cout << "더이상 항공을 추가할 수 없습니다.";
}
void stateAir(Air** air,  int& pCount){
	for (int i = 0; i < pCount; i++){
		air[i]->show();
		cout << endl;
	}
}

int main(){
	
	Air** air = new Air*[4];
	int pCount = 0;
	air[0] = new Air("서울","인천", 3, 4);
	air[0]->show();
	/*while (1){
		switch (menu()){
		case 1:
			addAir(air, pCount);
			break;
		case 2:
			stateAir(air, pCount);
			air[0]->show();
			break;
		case 3:
			break;
		case 4:
			return 0;
		}
	}
	*/return 0;
}