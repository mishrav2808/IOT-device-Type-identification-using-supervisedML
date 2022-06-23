
##########################################################
import os
import glob

#############################################################

labelFeature = open("IOT_label_feature.csv",'a') 
labelFeature.writelines("Label,IPLength,IPHeaderLength,TTL,\
           Protocol,SourcePort,DestPort,SequenceNumber,AckNumber\
           ,WindowSize,TCPHeaderLength,TCPLength,TCPStream\
     ,TCPUrgentPointer,IPFlags,IPID,IPchecksum,TCPflags,TCPChecksum\n")

##############################################################
print("filtering packets ...")
for original in glob.glob('original_pcap/*'):
    filename = original.split('/')[-1]
    print(f'filtering {filename} packets ..')
    for file in glob.glob(f"original_pcap/{filename}/*.pcap"):
        os.system("tshark -r " + file + " -w- -Y " + 'tcp' + ">> filtered_pcap/" +filename + ".pcap")

print("filtering completed")
###############################################################
print("extracting features..")
for filteredFile in glob.glob('filtered_pcap/*.pcap'):
    filename = filteredFile.split('/')[-1]
    label = filename.replace('.pcap', '')
    tsharkCommand = "tshark -r " + filteredFile + " -T fields \
                    -e ip.len -e ip.hdr_len -e ip.ttl \
                    -e ip.proto -e tcp.srcport -e tcp.dstport -e tcp.seq \
                    -e tcp.ack -e tcp.window_size_value -e tcp.hdr_len -e tcp.len \
                    -e tcp.stream -e tcp.urgent_pointer \
                    -e ip.flags -e ip.id -e ip.checksum -e tcp.flags -e tcp.checksum"

    all_features = str(os.popen(tsharkCommand).read())
    all_features = all_features.replace('\t',',')
    all_featuresList = all_features.splitlines()
    for features in all_featuresList:
        labelFeature.writelines(label + "," + features + "\n")

#############################################################
print("feature extraction  complete.")
print("----------DONE----------")


