from datetime import datetime


'''---------------------------------MemePage Class-----------------------------------------------'''
class MemePage:
    def __init__(self: 'MemePage', topic: str):
        """
        Initialize a MemePage object.

        Args:
            topic (str): The topic of the meme page.
        Examples:
        >>> meme = MemePage("CS61A")
        >>> (meme.members, meme.topic) == (0, "CS61A")
        True
        >>> type(meme.posts) == dict
        True
        """
        self.topic = topic
        self.members = 0
        self.posts = {}
        

    def __eq__(self: 'MemePage', other: 'MemePage') -> bool:
        """
        Compare the MemePage object with another MemePage object for equality.

        Args:
            other (MemePage): The other MemePage object to compare with.

        Returns:
            bool: True if the MemePage objects are equal, False otherwise.
        Examples:
        >>> meme1 = MemePage("Among Us")
        >>> meme2 = MemePage("Among Us")
        >>> meme1 == meme2
        True
        >>> meme1.members += 1 #Meme1 and meme2 do not equal since the member attributes are different
        >>> meme1 == meme2
        False
        >>> meme3 = MemePage("Spider Man")
        >>> meme2 == meme3
        False
        """
        return self.topic == other.topic and self.members == other.members 


'''---------------------------------MemberPage Class-----------------------------------------------'''

class Member:
    
    def __init__(self: 'Member', name: str, memepage: 'MemePage'):
        """
        Initialize a Member object.

        Args:
            name (str): The name of the member.
            memepage (MemePage): The MemePage object the member belongs to.
        Examples:
        >>> meme1 = MemePage("Among Us")
        >>> red = Member("Red", meme1)
        >>> blue = Member("Blue", meme1)
        >>> imposter = Member("grey", meme1)
        >>> red.name == "Red" and red.memepage == meme1
        True
        >>> meme1.members == 3 and imposter.memepage == meme1 == blue.memepage
        True
        """
        self.name = name
        self.memepage = memepage 
        self.memepage.members += 1
        self.activity = 0
        self.posts = 0


    def tag_ur_friend_in_meme(self: 'Member', friend: 'Member', title_of_post: str) -> str:
        """
        Tag a friend in a meme post.

        Args:
            friend (Member): The friend to tag in the meme.
            title_of_post (str): The title of the post to tag the friend in.

        Returns:
            str: A message indicating whether the friend was tagged or not.
        Examples:
        >>> meme1 = MemePage("Among Us")
        >>> meme2 = MemePage("Barbie")
        >>> red = Member("Red", meme1)
        >>> blue = Member("Blue", meme1)
        >>> grey = Member("Grey", meme2)
        >>> isinstance(blue, Member)
        True
        >>> imposter = Member("grey", meme1)
        >>> red.tag_ur_friend_in_meme(blue, "Who is the Imposter")
        "@Blue has been tagged in 'Who is the Imposter'"
        >>> red.activity == 1 and blue.activity == 0
        True
        >>> grey.tag_ur_friend_in_meme(blue, "Barbie is better than Oppenheimer!")
        'You cannot tag someone in a meme if they are not a member of this page.'
        >>> imposter.tag_ur_friend_in_meme(meme2, "Scuba Diving") #meme2 is not a member
        'Invalid input. Expected a Member object but received an object of a different type.'
        """
        if isinstance(friend, Member):
            if self.memepage == friend.memepage: 
                self.activity += 1
                return f"@{friend.name} has been tagged in '{title_of_post}'"
            else: 
                return f"You cannot tag someone in a meme if they are not a member of this page."
        else:
            return f"Invalid input. Expected a Member object but received an object of a different type."
        
        
    

    def post_in_page(self: 'Member', title_of_post: str) -> str:
        """
        Post a meme in the meme page.

        Args:
            title_of_post (str): The title of the post to be posted.
        Examples:
        >>> meme1 = MemePage("Among Us")
        >>> red = Member("Red", meme1)
        >>> blue = Member("Blue", meme1)
        >>> imposter = Member("grey", meme1)
        >>> len(meme1.posts) == 0
        True
        >>> title = "Red is the imposter! Vote for him!"
        >>> imposter.post_in_page(title)
        'Your total activity on this Among Us page is 1, and your total posts to it is now 1.'
        >>> title in imposter.memepage.posts
        True
        >>> blue.post_in_page(title)
        'You have been banned for reposting a meme.'
        >>> title in red.memepage.posts
        True
        >>> red.post_in_page("Imposter is kind of suspicious")
        'Your total activity on this Among Us page is 1, and your total posts to it is now 1.'
        >>> len(imposter.memepage.posts) == 2
        True
        """
        if not title_of_post in self.memepage.posts:
            self.memepage.posts.update({title_of_post: 0}) 
            self.activity += 1
            self.posts += 1
            return f"Your total activity on this {self.memepage.topic} page is {self.activity}, and your total posts to it is now {self.posts}."
        else:
            return f"You have been banned for reposting a meme." 


    def like_a_post_in_page(self: 'Member', title_of_post: str) -> str:
        """
        Like a post in the meme page. Throw an error if title of post is not found.

        Args:
            title_of_post (str): The title of the post to like.

        Returns:
            str: A message indicating the activity and number of likes on the post.
        Examples:
        >>> meme_page = MemePage("Computer Security")
        >>> alice = Member("Alice", meme_page)
        >>> bob = Member("Bob", meme_page)
        >>> mallory = Member("Mallory", meme_page)
        >>> password = "among us"
        >>> title = f"Hey Bob! My Netflix password is {password}"
        >>> alice.post_in_page(title)
        'Your total activity on this Computer Security page is 1, and your total posts to it is now 1.'
        >>> alice.tag_ur_friend_in_meme(bob, title)
        "@Bob has been tagged in 'Hey Bob! My Netflix password is among us'"
        >>> bob.like_a_post_in_page(title)
        "Your total activity on this Computer Security page is 1, and the total number of likes on the post 'Hey Bob! My Netflix password is among us' is 1."
        >>> mallory.like_a_post_in_page(title)
        "Your total activity on this Computer Security page is 1, and the total number of likes on the post 'Hey Bob! My Netflix password is among us' is 2."
        >>> bob.activity == 1 and bob.memepage.posts[title] == 2
        True
        >>> title2 = f"Hey Alice, the password doesn't seem to work :("
        >>> bob.post_in_page(title2)
        'Your total activity on this Computer Security page is 2, and your total posts to it is now 1.'
        >>> bob.tag_ur_friend_in_meme(alice, title2)
        "@Alice has been tagged in 'Hey Alice, the password doesn't seem to work :('"
        >>> del mallory.memepage.posts[title2]
        >>> title3 = "The new super mario movie is awesome!"
        >>> mallory.post_in_page(title3)
        'Your total activity on this Computer Security page is 2, and your total posts to it is now 1.'
        >>> bob.like_a_post_in_page(title3)
        "Your total activity on this Computer Security page is 4, and the total number of likes on the post 'The new super mario movie is awesome!' is 1."
        >>> alice.like_a_post_in_page(title2)
        "Title of post 'Hey Alice, the password doesn't seem to work :(' not found"
        """
        if title_of_post in self.memepage.posts.keys():
            self.memepage.posts[title_of_post] += 1
            self.activity += 1
            return f"Your total activity on this {self.memepage.topic} page is {self.activity}, and the total number of likes on the post '{title_of_post}' is {self.memepage.posts[title_of_post]}."

        else:
            return f"Title of post '{title_of_post}' not found" 
