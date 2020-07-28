from eccodes import *
import sys 
def main():
    print(codes_get_api_version())
    if ( len( sys.argv) != 2):
        print(f" usage {sys.argv[0]} bufr file")
    else:
        fname=sys.argv[1]
        f=open(fname,"rb")
        nmsg=codes_count_in_file(f)
        print(f"number of message {nmsg}")
        f.close()


if __name__=="__main__":
    main()
