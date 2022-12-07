using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Xml;
using System.Xml.Linq;
using System.Text.Json;


namespace ConsoleApp1
{
    class Program
    {
        class Node
        {
            public int id { get; set; } = 0;
            public int parentId { get; set; } = 0;
            public List<Node> children { get; set; } = new List<Node>();
        }

        static void Main(string[] args)
        {

            List<Node> lstNodes = new List<Node>();
            lstNodes.Add(new Node() { id=56, parentId=62 });
            lstNodes.Add(new Node() { id=81, parentId=80 });
            lstNodes.Add(new Node() { id=74, parentId=0 });
            lstNodes.Add(new Node() { id=76, parentId=80 });
            lstNodes.Add(new Node() { id=63, parentId=62 });
            lstNodes.Add(new Node() { id=80, parentId=86 });
            lstNodes.Add(new Node() { id=87, parentId=86 });
            lstNodes.Add(new Node() { id=62, parentId=74 });
            lstNodes.Add(new Node() { id=86, parentId=74 });

            IDictionary<int, int> idMapping = new Dictionary<int, int>();

            short index = 0;
            foreach(Node i in lstNodes)
            {
                idMapping[i.id] = index;
                index++;
            }

            Node rootNode = null;
            lstNodes.ForEach(node => {

                // Handle the root element
                if (node.parentId == 0)
                {
                    rootNode = node;
                    return;
                }

                if (node.parentId != 0)
                {
                    // Use our mapping to locate the parent element in our data array
                    Node parentEl = lstNodes[idMapping[node.parentId]];

                    // Add our current el to its parent's `children` array
                    List<Node> children = new List<Node>();
                    parentEl.children.ToList().ForEach(child => { children.Add(child); });
                    children.Add(node);

                    parentEl.children = children;
                }

            });

            Console.WriteLine(JsonSerializer.Serialize(rootNode));


        }

    }
}
