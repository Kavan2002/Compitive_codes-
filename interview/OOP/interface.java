package interview;

//Java Program to Demonstrate Concept of interfaces

//Interface
interface salary {
	void insertsalary(int salary);
}

//Class 1
//Implementing the salary in the class
class SDE1 implements salary {
	int salary;
	
//	include bonus
	@Override public void insertsalary(int salary)
	{
		this.salary = salary + 20000; 
	}
	void printSalary() { System.out.println(this.salary); }
}

//Class 2
//Implementing the salary inside the SDE2 class
class SDE2 implements salary {
	int salary;
	@Override public void insertsalary(int salary)
	{
		this.salary = salary + 15000;
	}
	void printSalary() { System.out.println(this.salary); }
}

public class Interface {

	public static void main(String[] args)
	{
		SDE1 ob = new SDE1();
		// Insert different salaries
		ob.insertsalary(10000);
		ob.printSalary();
		
		SDE2 ob1 = new SDE2();
		ob1.insertsalary(200000);
		ob1.printSalary();
	}
}
