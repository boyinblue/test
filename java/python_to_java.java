import java.util.Scanner;

public class python_to_java
{
	public static void main(String[] args)
	{
		System.out.print("입력할 줄 갯수 입력: ");
		Scanner scanner = new Scanner(System.in);
		int line = scanner.nextInt();
		int iSumCpu = 0;
		int iSumFinish = 0;
		int iInput = 0;

		for( int i = 0 ; i < line ; i++)
		{
			for( int j = 0 ; j < 1000 ; j++ )
			{
				iInput = scanner.nextInt();
				if( iInput == -1 )
				{
					break;
				}

				iSumFinish += iInput;
				if( j % 2 == 1 )
				{
					iSumCpu += iInput;
				}
			}
		}
		System.out.printf("%d %d", iSumCpu, iSumFinish);
	}

}

