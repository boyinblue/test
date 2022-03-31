
public class change_lower_case_to_uppser_case
{
  public static void main(String[] args)
  {
    char chLowerCase = 'c';
    char chUpperCase = (char)( (int)chLowerCase - 0x20 );

    System.out.printf("%c", chUpperCase);
  }
}
