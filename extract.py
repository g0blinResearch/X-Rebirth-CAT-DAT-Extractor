import os
outdir = "out"
list_of_files = [file for file in os.listdir(
    ".") if file.lower().endswith(".cat")]
for catfile in list_of_files:
    inf = open(catfile, "rb")
    inf_data_name = "%s.dat" % catfile.split(".")[0]
    inf_data = open(inf_data_name, "rb")

    for line in inf:
        obj_data_split = line.split(" ")
        filepath = " ".join(obj_data_split[0:len(obj_data_split) - 3])
        obj_data = {"hash": obj_data_split[-1],
                    "modified_epoch": obj_data_split[-2],
                    "size": obj_data_split[-3],
                    "filepath": filepath}
        obj_data["path"] = os.path.dirname(obj_data["filepath"])
        obj_data["filename"] = obj_data["filepath"].split("/")[-1]

        if not os.path.isdir("%s/%s" % (outdir, obj_data["path"])):
            os.makedirs("%s/%s" % (outdir, obj_data["path"]))

        try:
            outf = open("%s/%s/%s" %
                        (outdir, obj_data["path"], obj_data["filename"]), "wb")
            outf.write(inf_data.read(int(obj_data["size"])))
            outf.close()
        except IOError:
            print("[IOERROR] %s/%s/%s" %
                 (outdir, obj_data["path"], obj_data["filename"]))
    inf.close()
