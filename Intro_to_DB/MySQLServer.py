import pymysql

try:
    # Connect to MySQL server (without specifying database)
    mydb = pymysql.connect(
        host="localhost",
        user="Josiah Obeng",          # change if your MySQL user is different
        password="0542775386@Obeng"
    )

    mycursor = mydb.cursor()

    # Create database if it doesn't exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("✅ Database 'alx_book_store' created successfully!")

except Exception as e:
    print("❌ Error:", e)

finally:
    # Close connection if open
    try:
        mycursor.close()
        mydb.close()
    except:
        pass
