//
//  ViewController.swift
//  NinjaGold
//
//  Created by Jaeson Booker on 3/8/17.
//  Copyright © 2017 Jaeson Booker. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var count = 100
    var health = 100
    @IBOutlet weak var score: UILabel!
    @IBOutlet weak var status: UILabel!
    @IBOutlet weak var status2: UILabel!
    @IBOutlet weak var status1: UILabel!
    @IBOutlet weak var status3: UILabel!
    @IBOutlet weak var healthcount: UILabel!
    @IBAction func building(_ sender: UIButton) {
        if sender.tag == Int(1) {
            if health < 1 {
                status1.text = "You're dead."
            }
            else {
                status1.text = "Remember your failure at the cave!"
                count += 5
                health -= 10
                score.text = String(count)
                healthcount.text = String(health)
            }
        }
        if sender.tag == Int(2) {
            if health < 1 {
                status2.text = "You're dead, loser"
            }
            else {
                status2.text = "This button is the best button."
                count -= Int(arc4random_uniform(150))
                count += Int(arc4random_uniform(100))
                if count == 0 {
                    status2.text = "Loser!"
                }
                if count < 0 {
                    status2.text = "Where's my money??"
                    health -= 50
                }
                score.text = String(count)
                healthcount.text = String(health)
            }
        }
        if sender.tag == Int(3) {
            if health < 1 {
                status3.text = "You're dead, Jim"
            }
            else {
                status3.text = "Your house... in the middle of the street."
                count += 10
                score.text = String(count)
                healthcount.text = String(health)
            }
        }
        if sender.tag == Int(4) {
            if health < 1 {
                status.text = "Dead, dead, dead"
            }
            else {
                status.text = "It's a farm... it's kinda lame."
                count += 2
                health -= 10
                score.text = String(count)
                healthcount.text = String(health)
            }
        }
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        score.text = String(count)
        healthcount.text = String(health)
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

