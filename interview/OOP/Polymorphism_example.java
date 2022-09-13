package interview;

class A1{

	int amt;
	String s;
	
	public A1(){
		
		this.amt = 200;
		this.s = "Name: ";
	}
	
	public A1(int i , String d){
		
		this.amt = i;
		this.s = d;
	}
	
	public void  add_variable(int i)
	{
		System.out.println(this.amt+i);
	}
	
	public void  add_variable(String i)
	{
		System.out.println(this.s+i);
	}
}


class super_class{
	
	void super_class_method(){
		
		System.out.println("it is super class method");
		
	}
	
}

class sub_class extends super_class{
	
	@Override
	void super_class_method(){
		
		System.out.println("it is sub class method");
		
	}
	
}


public class Polymorphism_example{
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//	static polymorphism	
		A1 obj_a1 = new A1();
		obj_a1.add_variable(50);
		obj_a1.add_variable("kavan ardeshana");
		
		System.out.println("\nparameterised constructor");
	
		A1 obj_a2 = new A1(20,"krishna");
		obj_a2.add_variable(50);
		obj_a2.add_variable("kavan ");
		
// run time polymorphism 
		super_class superClass = new sub_class();
        
        superClass.super_class_method();        //Output : Super_Class_Method
         
        superClass = new sub_class();		
         
        superClass.super_class_method();
		
//        sub_class s1 = new super_class();
//        We can use superclass reference to hold any subclass object derived from it.
        
//      By using superclass reference, we will have access only to those 
//      parts(methods and variables) of the object defined by the superclass.   
//        https://www.geeksforgeeks.org/referencing-subclass-objects-subclass-vs-superclass-reference/#:~:text=First%20approach%20(Referencing%20using%20Superclass,method%20that%20will%20be%20executed.
	}

}
