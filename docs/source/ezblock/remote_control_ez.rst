Remote Control
==================

You can also use the widgets on Ezblock Studio to make PiSloth move.

.. image:: media/remote_control_pic.jpg

* `How to Use the Remote Control Function? <https://docs.sunfounder.com/projects/ezblock3/en/latest/remote.html>`_

**TIPS**

To use the remote control function, you need to enter the **Remote Control** page from the left side of main page, and then drag one D-pad and 4 buttons to the central area.

.. image:: media/control3.png

Back in the programming page, you will see an additional Remote category, and the D-pad and Button block appear in it.

* **Button () get value**: This block is used to read the value of the buttons, if the button is pressed, the value is 1, otherwise it is 0.
* **Button () is (press/release)**: This block and ``Button () get value = (0/1)`` have the same effect and can be used directly to determine whether a button is pressed or not.
* **D-pad () get () value**: This block is used to read the up/down/left/right (selected through the drop-down menu) pad values, press for 1 and release for 0.

.. image:: media/control4.png
  :width: 500


**EXAMPLE**

.. image:: media/control.png