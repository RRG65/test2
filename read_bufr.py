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
        k=1
        for i in range(nmsg):
            bid=codes_bufr_new_from_file(f)
            codes_set(bid,"unpack",1)
            try:
                airTemp=codes_get(bid,f"#{k}#airTemperature")
                print(airTemp)
            except Exception as e:
                print(e)
            codes_release(bid)
            k+=1
        f.close()


if __name__=="__main__":
    main()
