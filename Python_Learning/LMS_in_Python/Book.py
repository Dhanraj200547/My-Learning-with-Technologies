class Book():
    def __init__(self,id,title,author):
        self.id = id
        self.title = title
        self.author = author
        self.isIssued = False
    
    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def isIssued(self):
        return self.isIssued
    
    def issueBook(self):
        if not self.isIssued:
            self.isIssued = True
            print("Book " + self.title + " is issued Successfully")
        else:
            print("Book "+ self.title + " is already issued")
    
    def returnBook(self):
        if self.isIssued:
            self.isIssued = False
            print("Book " + self.title + " is returned succesfully")
        else:
            print("Book "+ self.title + "was not issued")