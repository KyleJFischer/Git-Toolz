class PullRequestTemplate:
    header = ""
    content = ""
    
    def __init__(self, header, content):
        self.header = header
        self.content = content


    def replaceStringsInTemplates(self, variables):
        replacedHeader = self.putVariablesInString(self.header, variables)
        replacedContent = self.putVariablesInString(self.content, variables)
        return (replacedHeader, replacedContent)

    def putVariablesInString(self, inputString, variables):
        return inputString.format(**variables)