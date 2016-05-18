import static org.junit.Assert.*;

import org.junit.Test;


public class PalindromeTest {

	@Test
	public void testIsPalindrome() {
		assertTrue(Palindrome.isPalindrome("Able was I ere I saw Elba"));
		assertTrue(Palindrome.isPalindrome("A man, a plan, a canal - Panama!"));
		assertTrue(Palindrome.isPalindrome("Madam in Eden, I'm Adam"));
		assertTrue(Palindrome.isPalindrome("Doc, note: I dissent. A fast never prevents a fatness. I diet on cod"));
		assertTrue(Palindrome.isPalindrome("Never odd or even"));
		
		assertTrue(Palindrome.isPalindrome("121"));
		assertTrue(Palindrome.isPalindrome("noon"));
		assertTrue(Palindrome.isPalindrome("Rise to vote, sir"));
		assertTrue(Palindrome.isPalindrome("doodood"));
		// Negative cases
		assertFalse(Palindrome.isPalindrome("doodoo"));
		assertFalse(Palindrome.isPalindrome("De f is! not a palINDOME9874GK"));
		assertFalse(Palindrome.isPalindrome("Able was I eere I saw Elba"));
		assertFalse(Palindrome.isPalindrome("adam in Eden, I'm Adam"));
		assertFalse(Palindrome.isPalindrome("Never odd or eve"));
	}

}
