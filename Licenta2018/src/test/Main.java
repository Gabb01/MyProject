package test;

class A 
{
	private int y = 10;
	
	public int metoda()
	{
		return y;
	}
}
class Test<T extends A> {
	private T x;
	
	public Test(T t)
	{
		x = t;
	}

	public int metoda() {
		return 5 + x.metoda();
	}
}

public class Main 
{
	public static void main(String[] args)
	{
		A a = new A();
		
		Test<A> b = new Test<A>(a);
		System.out.println(b.metoda());
	}
}