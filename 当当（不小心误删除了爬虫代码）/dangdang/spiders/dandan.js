using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using MongoDB.Bson;
using MongoDB.Driver;
 
namespace Mongodb
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            Init();
        }
        //数据库连接字符串
        const string strconn = "mongodb://127.0.0.1:27017";
        //数据库名称
        const string dbName = "test";
        MongoServer server;
        MongoDatabase db;
        void Init()
        {
            //创建数据库链接
            server = MongoDB.Driver.MongoServer.Create(strconn);
            //获得数据库
            db = server.GetDatabase(dbName);
        }
 
        private void btnSave_Click(object sender, EventArgs e)
        {
            SaveDocToMongo(@"d:\quwenzhe.docx");
        }
 
        private void btnShow_Click(object sender, EventArgs e)
        {
            GetDocFromMongo(@"E:\newquwenzhe.doc");
        }
 
        /// <summary>
        /// 保存Word到Mongo
        /// </summary>
        /// <param name="filename">需要保存的文件名</param>
        private void SaveDocToMongo(string filename)
        {
            byte[] byteDoc = File.ReadAllBytes(filename);
            BsonDocument doc = new BsonDocument();
            doc["id"] = "1";
            doc["content"] = byteDoc;
            MongoCollection col = db.GetCollection("doc");
            col.Save(doc);
        }
 
        /// <summary>
        /// 将Mongo中的Word保存到本地
        /// </summary>
        /// <param name="filename">保存到本地的文件名</param>
        private void GetDocFromMongo(string filename)
        {
            MongoCollection col = db.GetCollection("doc");
            var query = new QueryDocument { { "id", "1" } };
            var result = col.FindAs<BsonDocument>(query);
            byte[] buff = (byte[])((BsonDocument)result.ToList()[0]).GetValue("content");
            FileStream fs;
            FileInfo fi = new FileInfo(filename);
            fs = fi.OpenWrite();
            fs.Write(buff, 0, buff.Length);
            fs.Close();
        }
    }
}
