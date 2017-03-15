//
//  ViewController.swift
//  coldashell
//
//  Created by Jaeson Booker on 3/8/17.
//  Copyright © 2017 Jaeson Booker. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var namecount = 0
    var name = ["Leaf Erikson", "Madmax",
                "Chuck Norris", "Bruce Lee",
                "Bruce Wayne", "Bruce Banner",
                "Clark Kent", "Peter Parker",
                "Mary Jane", "Golly Gee",
                "Robin Hood"]
    @IBOutlet weak var doit: UILabel!
    @IBOutlet weak var count: UILabel!
    @IBAction func buttonohbutton(_ sender: Any) {
        namecount = Int(arc4random_uniform(10))
        doit.text = name[namecount]
        count.text = String(namecount)
        if namecount < 5 {
            count.textColor = #colorLiteral(red: 0.9254902005, green: 0.2352941185, blue: 0.1019607857, alpha: 1)
        }
        else {
            count.textColor = #colorLiteral(red: 0.4666666687, green: 0.7647058964, blue: 0.2666666806, alpha: 1)
        }
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

