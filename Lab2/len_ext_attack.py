from pymd5 import md5, padding
import urllib

def GenerateToken(prevToken, append, totalBits):
    newHash = md5(state=prevToken.decode("hex"), count=totalBits)
    apnd = append
    newHash.update(apnd)
    newToken = newHash.hexdigest()
    return newToken

def ParseURL(url):
    preToken = url[:url.find("=") + 1]
    prevHash = url[url.find("=") + 1:url.find("&")]
    command = url[url.find("&") + 1:]
    return preToken, prevHash, command




if __name__ == "__main__":

    #Known Information
    url = open('3.3_url.txt','r').read()
    preToken, prevHash, command = ParseURL(url)
    passLen = 8
    passCmdLen = passLen + len(command)
    pad = padding(passCmdLen * 8)
    paddingLen = len(pad)
    bits = (passCmdLen + paddingLen) * 8
    print("Original url: " + url)
    print("Pre hash url: " + preToken)
    print("Current hash: " + prevHash)
    print("Command string: " + command)
    print ("Message length(padded):" + str(bits) + ' bits')


    #Length Extension Attack
    append = open('3.3_command3.txt').read()
    newToken = GenerateToken(prevHash, append, bits)
    urlPadding = urllib.quote(pad)
    newCommand = command + urlPadding + append
    newURL = preToken + newToken + "&" + newCommand
    print("URL Padding: " + urlPadding)
    print("New token: " + newToken)
    print("Generated url: " + newURL)
    open('solution33.txt', 'w').write(newURL)


    #Verifying
    from verify_len_ext import verify
    print('\n'  + 'Enter secret key, data and appending message to verify LEA authentication...')
    key = raw_input('key: ')
    data = raw_input('data: ')
    append = raw_input('append: ')
    verify(key,data,append)