from visualdl import LogWriter


class LoggerScalar:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def scalar(self, tag, step, value):
        assert self.base_dir is not None, 'Please set base_dir first'
        with LogWriter(logdir=self.base_dir) as writer:
            writer.add_scalar(tag, value, step)

    def plot_data(self, my_fantastic_logging):
        assert self.base_dir is not None, 'Please set base_dir first'
        epoch = min([len(i) for i in my_fantastic_logging.values()])
        with LogWriter(logdir=self.base_dir) as writer:
            writer.add_scalar(
                tag="loss/train",
                step=epoch,
                value=my_fantastic_logging['train_losses'][-1]
            )
            writer.add_scalar(
                tag="loss/val",
                step=epoch,
                value=my_fantastic_logging['val_losses'][-1]
            )
            writer.add_scalar(
                tag="dice/fg/mean",
                step=epoch,
                value=my_fantastic_logging['mean_fg_dice'][-1]
            )
            writer.add_scalar(
                tag="dice/fg/ema",
                step=epoch,
                value=my_fantastic_logging['ema_fg_dice'][-1]
            )
            writer.add_scalar(
                tag="epoch/duration",
                step=epoch,
                value=my_fantastic_logging['epoch_end_timestamps'][-1] - my_fantastic_logging['epoch_start_timestamps'][-1]
            )
            writer.add_scalar(
                tag="learning_rate",
                step=epoch,
                value=my_fantastic_logging['lrs'][-1]
            )