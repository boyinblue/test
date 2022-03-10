import java.util.Scanner;

public class scanner_if
{
	public static void practice8()
	{
		System.out.print("주민번호를 입력하세요(- 포함) : ");
	
		Scanner scanner = new Scanner(System.in);

		String input = scanner.nextLine();
		String substring = input.substring(7,8);

		if ( substring.equals("1") || substring.equals("3") )
		{
			System.out.print("남자");
		}
		else if ( substring.equals("2") || substring.equals("4") )
		{
			System.out.print("여자");
		}
		else
		{
			System.out.print("에러");
		}
	}

	public static void main(String[] args)
	{
		practice8();
	}
}
