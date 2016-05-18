
public class Palindrome {

	public static boolean isPalindrome(String word){
		word = word.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
		for (int i = word.length() -1, j = 0; i > j; i--, j++){
			if (word.charAt(j) != word.charAt(i))
				return false;
		}
		return true;
	}

}
