from configparser import RawConfigParser
import psycopg2
from project.output.relation import Relation
from project.output.mfstructure import MF_Structure


def main():
    configFile = "/Users/shubhamjain/CS562/project/db.properties"
    configPar = RawConfigParser()
    configPar.read(configFile)
    configuration = dict(configPar.items("DatabaseSection"))
    conn = psycopg2.connect(database=configuration['database'], user=configuration['user'],
                            password=configuration['password'], host=configuration['host'], port=configuration['port'])
    cur = conn.cursor()
    print('Database connected Successfully')
    mfStructure = []
    cur.execute("select * from sales")
    rows = cur.fetchall()
    for row in rows:
        relation = Relation()
        relation.setAllVal(row)
        addToMF = True
        for eachMF in mfStructure:
            if eachMF.getCust() == relation.getCust():
                addToMF = False
                break
        if addToMF:
            addToMF = False
            mf = MF_Structure()
            mf.setCust(relation.getCust())
            mf.set_1_sum_quant(0)
            mf.set_1_count_quant(0.000001)
            mf.set_1_sum_quant(0)
            mf.set_2_sum_quant(0)
            mf.set_3_sum_quant(0)
            mf.set_3_count_quant(0.000001)
            mf.set_3_sum_quant(0)
            mfStructure.append(mf)

    cur.execute("select * from sales")
    rows = cur.fetchall()
    for row in rows:
        relation = Relation()
        relation.setAllVal(row)
        for index, mfs in enumerate(mfStructure):
            if (relation.getCust() == mfs.getCust()) and (relation.getState() == "NY"):
                mfs.set_1_sum_quant(mfs.get_1_sum_quant() + relation.getQuant())
                mfStructure[index] = mfs
                mfs.set_1_count_quant(mfs.get_1_count_quant() + 1)
                mfStructure[index] = mfs

    cur.execute("select * from sales")
    rows = cur.fetchall()
    for row in rows:
        relation = Relation()
        relation.setAllVal(row)
        for index, mfs in enumerate(mfStructure):
            if (relation.getCust() == mfs.getCust()) and (relation.getState() == "NJ"):
                mfs.set_2_sum_quant(mfs.get_2_sum_quant() + relation.getQuant())
                mfStructure[index] = mfs

    cur.execute("select * from sales")
    rows = cur.fetchall()
    for row in rows:
        relation = Relation()
        relation.setAllVal(row)
        for index, mfs in enumerate(mfStructure):
            if (relation.getCust() == mfs.getCust()) and (relation.getState() == "CT"):
                mfs.set_3_sum_quant(mfs.get_3_sum_quant() + relation.getQuant())
                mfStructure[index] = mfs
                mfs.set_3_count_quant(mfs.get_3_count_quant() + 1)
                mfStructure[index] = mfs

    delete = []
    for idx, mfs in enumerate(mfStructure):
        if not ((mfs.get_1_sum_quant()) > (2 * mfs.get_2_sum_quant()) or (
                mfs.get_1_sum_quant() / mfs.get_1_count_quant()) > (mfs.get_3_sum_quant() / mfs.get_3_count_quant())):
            delete.append(mfs)
    for mfs in delete:
        mfStructure.remove(mfs)
    print('{0:9s}'.format('cust'), end='   ')
    print('{0:12s}'.format('1_sum_quant'), end='   ')
    print('{0:12s}'.format('2_sum_quant'), end='   ')
    print('{0:12s}'.format('3_sum_quant'), end='   ')
    print()
    print("=========", end="   ")
    print("============", end="   ")
    print("============", end="   ")
    print("============", end="   ")
    print()
    for idx, mfs in enumerate(mfStructure):
        print("{0:9s}".format(mfs.getCust()), end="   ")
        print("{0:12f}".format(mfs.get_1_sum_quant()), end="   ")
        print("{0:12f}".format(mfs.get_2_sum_quant()), end="   ")
        print("{0:12f}".format(mfs.get_3_sum_quant()), end="   ")
        print()


if __name__ == '__main__':
    main()
