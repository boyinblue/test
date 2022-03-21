public class FuelCalculator
{
	public double calcByKilo( int kilo, double liter )
	{
		return kilo / liter;
	}

	public static void main(String[] args)
	{
		int kilo;
		double liter, kpl;

		FuelCalculator caculator = new FuelCalculator();
		liter = Double.parseDouble(args[0]);
		kilo = Integer.parseInt(args[1]);

		System.out.println("연비 계산 프로그램입니다. \n");
		System.out.println("입력된 거리 : " + kilo);

		System.out.println("입력된 휘발류 양 : " + liter);

		kpl = caculator.calcByKilo( kilo, liter );
		System.out.println("Kilometer per liter : "+ kpl );
	}
}
