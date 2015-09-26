import socket


def whois(query, hostname="chi.ninux.org"):
    """ Perform a basic whois request, from
        http://code.activestate.com/recipes/577364-whois-client/ """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, 43))
    s.send(query + "\r\n")
    response = ''
    while True:
        d = s.recv(4096)
        response += d
        if not d:
            break
    s.close()
    fields = {}
    for line in response.split('\n'):
        if "mapserver:" in line:
            fields["mapserver"] = line.replace(' ', '').split(":")[1]
    return fields
