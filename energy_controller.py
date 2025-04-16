class PIDController:
    def __init__(self, K_p, K_i, K_d, target):
        """
        Initialize the PID controller.
        
        Args:
            K_p (float): Proportional gain
            K_i (float): Integral gain
            K_d (float): Derivative gain
            target (float): Target value
        """
        self.K_p = K_p
        self.K_i = K_i
        self.K_d = K_d
        self.target = target
        self.integral = 0
        self.previous_error = 0

    def update(self, measurement, dt):
        """
        Update the controller and return the control signal.
        
        Args:
            measurement (float): Current measured value
            dt (float): Time step (s)
        
        Returns:
            float: Control signal (ds/dt)
        """
        error = measurement - self.target
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt if dt > 0 else 0
        output = self.K_p * error + self.K_i * self.integral + self.K_d * derivative
        self.previous_error = error
        return output
