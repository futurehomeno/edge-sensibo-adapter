import sys

def set_deb_control(version , arch):
    file_name  = "./package/debian/DEBIAN/control"
    template = "Package: sensibo\n"
    template+= "Version: "+version+"\n"
    template+= "Section: non-free/misc\n"
    template+= "Priority: optional\n"
    template+= "Architecture: "+arch+"\n"
    template+= "Maintainer: Tor Erik Skaardal <skardal@hey.com>\n"
    template+= "Description: Control Sensibo Sky from futurehome.\n"

    f = open(file_name,"w")
    f.write(template)
    f.close()


def set_version_file(version):
    file_name = "./VERSION"
    f = open(file_name,"w")
    f.write(version)
    f.close()    


if __name__ == "__main__":
   environment = sys.argv[1] 
   version = sys.argv[2]
   arch = sys.argv[3]
   set_deb_control(version,arch)
   set_version_file(version)