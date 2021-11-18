import java.util.Scanner;

public class javaCli {

  static Scanner scan;

  public static void main(String[] args) {
    scan = new  Scanner(System.in);
    mainMenu();
  }

  public static void mainMenu (){
    System.out.println("Welcome! Please select an option:");

    System.out.println("0: Exit");
    System.out.println("1: Camel case a string");

    int input = scan.nextInt();

    switch(input) {
      case 0:
        System.exit(0);
        break;

      case 1:
        camelCase();


    }
  }

  public static void camelCase(){
    System.out.println("Enter a sentence:");
    String text = scan.nextLine();

    StringBuilder builder = new StringBuilder();
    char delim = ' ';
    boolean shouldConvertNextCharToLower = true;

    for (int i = 0; i < text.length(); i++) {
      char currentChar = text.charAt(i);
      if (currentChar == delim) {
          shouldConvertNextCharToLower = false;
      } else if (shouldConvertNextCharToLower) {
          builder.append(Character.toLowerCase(currentChar));
      } else {
          builder.append(Character.toUpperCase(currentChar));
          shouldConvertNextCharToLower = true;
      }
    }
    System.out.println(builder.toString());
  }


}
