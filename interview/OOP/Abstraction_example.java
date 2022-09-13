package interview;

//
abstract class interest{
	
	abstract void calc_interest(int amnt);
	
}

class saving extends interest{

	int interest_rate = 5;
	int years = 2 ; 
	@Override
	void calc_interest(int amnt) {
		// TODO Auto-generated method stub
		System.out.println("interest is alllowed ");
		System.out.println("interest rate : 5%\nyears : 1year");
		
		float i_amnt = (amnt*interest_rate*years)/100;
		
		System.out.println("interest amount : "+i_amnt);
	}
	
}

class current extends interest{

	int interest_rate = 0; 
	
	@Override
	void calc_interest(int amnt) {
		// TODO Auto-generated method stub
		System.out.println("insterest isn't available in current account");
	}
	
}
public class Abstraction_example {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String type = "S";
		
		if (type.equals("S")){
			
			saving s = new saving();
			s.calc_interest(5000);
		}
		else{
			current s = new current();
			s.calc_interest(10000);
		}
		
//		s.calc_interest();
	}

}

