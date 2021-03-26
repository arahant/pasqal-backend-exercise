# Backend developer interview exercice @ Pasqal

During this exercise, you will be buliding a job scheduler for our pool of devices.

You are allowed to use everything from python standard library.

## Get started

You can start by creating a virtual environment and activating it

```bash
python3 -m venv venv
source ./venv/bin/activate
```

Then, install the package and run the [main function](exercise/__main__.py)

```bash
python3 setup.py develop
```

You can also launch the tests with

```bash
nosetests exercise/tests
```

Running the flask app
```
FLASK_APP=exercise:app flask run
./exercise/test.sh
```


## Definitions

We have a set of exotic devices (QPUs) that we are hosting ourselves. We will give access to theses devices through a cloud platform, letting users run their programs on our devices.

- A QPU is a device defined by a size and an ID. It runs client jobs **sequentially**.
- A job is a sequence of instructions to be run by a QPU. After running the job, the QPU returns a set of results on the form of a bit strings.
- A program is a set of jobs with a given priority. Programs with the highest priority will pass first.

Our scheduler will have 2 roles:

- scheduling jobs on the right QPUs
- managing the pool of QPUs

Remarks

- Jobs and programs are defined to run on a given device type (see `Job.device_type` and `Program.device_type`).
- Don't hesitate to update the already existing classes at any moment if you need to.
- The main function of the program can be found in (**main**.py)[exercice/__main__.py]. All the components and features of the exercise should run in a single program.
- For simplicity, we will mock calls to the actual QPUs using `Device.send` in [device.py](exercise/device.py) and calls to the users with the function `handle_result` defined in [utils](exercise/utils.py). We assume that later these functions would be replaced by actual http clients.
- Don't hesitate to write some [tests](exercice/tests) to help you with the coding. As an example, you can find a tests for the priority queue.
- The script [test.sh](test.sh) contains some examples of API calls

## Question 1: Pool manager

The scheduler is going to manage the pool of QPUs he has. In order to do this, we will keep at all times a trace of which device is available,
and what are its properties (described by the `Device` class). For that, we created the `DevicePool` class.

The scheduler will communicate via http with the devices. Whenever a new device is online, it will make a call to the scheduler to register itself.

Implement an [API service](exercise/api.py) that will let us add and remove devices to the pool. You can use any python web framework you like for this (e.g. Flask).
You will have to implement at least a route to add devices to the pool and another one to remove them.

Hint: Make sure the API server is running in an asynchronous way (e.g. using `threading` or `asyncio`) so that the scheduler can keep on doing its work.

## Question 2: Queue

Our QPUs are a scarce resource: we don't have many of them and they are pretty slow. This means that the client request load will most likely be much higher than
the rate at which we can treat their jobs. In order to handle the load, we will implement a priority queue.

Instead of using the python queue module, implement your own [ProcessQueue](exercise/queue.py) class with the following specs:

- Users can push items with a priority to the queue
- When popping an item from the queue, we get the item with the highest priority. If there are many, we return the oldest.

## Question 3: Workers

We are now going to use the queue we just created as a buffer for client jobs. In order to do that, we need 2 parts:

- A publisher that will add jobs to the queue. We will create additional API endpoints to let users manually add jobs to the queue.
- subscribers that will treat jobs. You can create a worker whose role will be to pop jobs from the queue, send them to the device,
  wait for a response, and send back the response to the user.

a) Create additional API endpoints to let users push jobs to the job queue
b) Implement a worker which role will be to pop jobs from the queue and send them to the devices.
