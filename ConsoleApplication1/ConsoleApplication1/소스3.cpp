//#include<iostream>
//using namespace std;
//class Node{
//public:
//	int key;
//	Node* next;
//};
//class linkedlist{
//private:
//	Node* head;
//	Node* tail;
//public:
//	linkedlist();
//	~linkedlist();
//	void insert(int key);// 스택구조
//	void insert2(int key);//q구조
//	void insert3(int key);//정렬
//	void showlist();
//	Node* find_node(int key);
//	Node* getTail();
//	void deletenode(int key);
//};
//linkedlist::linkedlist(){
//	head =new Node;
//	tail =new Node;
//	head->next = tail;
//	tail->next = tail;
//}
//linkedlist::~linkedlist(){
//	Node* s = head;
//	Node* r = s->next;
//	while (s != tail){
//		delete s;
//		s = r;
//		r = r->next;
//	}
//	delete s;
//	head = NULL;
//	tail = NULL;
//}
//void linkedlist::insert(int key){
//	Node* r = new Node;
//	r->key = key;
//	r ->next = head->next;
//	head->next = r;
//}
//void linkedlist::insert2(int key){
//	Node* r = new Node;
//	r->key = key;
//	r->next = tail;
//	Node *s= head;
//	while (s->next != tail){
//	//	cout << s->key << endl;
//		s = s->next;
//	}
//	s->next = r;
//}
//void linkedlist::showlist(){
//	Node* s =head->next;
//	while (s != tail){
//		cout << s->key << endl;
//		s = s->next;
//	}
//}
//void linkedlist::insert3(int key){
//	Node* r = new Node;
//	r->key = key;
//	Node* p = head;
//	Node* s = p->next;
//	while (s != tail&& s->key < r->key)
//	{
//		p = s;
//		s = s->next;
//	}
//	r->next = s;
//	p->next = r;
//}
//Node* linkedlist::find_node(int key){
//	Node* s = head->next;
//	while (s != tail&& s->key != key){
//		s = s -> next;
//	}
//	return s;
//}
//
//Node* linkedlist::getTail(){
//	return tail;
//}
//void linkedlist::deletenode(int key){
//	Node* p = head;
//	Node* s = p->next;
//	while (s != tail&&s->key!=key){
//		p = s;
//		s = s -> next;
//	}
//	if (s != tail){
//		p->next = s->next;
//		delete s;
//	}
//}
//
//////////////////////////////////////////////////////////////////////////////////////////
//int main(){
//	cout << "Stack" << endl;
//	linkedlist list;
//	list.insert(10);
//	list.insert(20);
//	list.insert(30);
//	list.insert(40);
//	list.insert(50);
//	list.showlist();
//
//	cout << "Queue" << endl;
//	linkedlist queue;
//	queue.insert2(10);
//	queue.insert2(20);
//	queue.insert2(30);
//	queue.insert2(40);
//	queue.insert2(50);
//	queue.insert2(60);
//	queue.showlist();
//	
//
//	cout << "Sorted List" << endl;
//	linkedlist list1;
//	list1.insert3(25);
//	list1.insert3(40);
//	list1.insert3(22);
//	list1.insert3(45);
//	list1.insert3(51);
//	list1.insert3(60);
//	list1.showlist();
//	Node* result=list1.find_node(45);
//	if (result != list1.getTail()){
//		cout << result->key <<"there is" << endl;
//
//	}
//	else
//		cout << "no exist" << endl;
//	return 0;
//}