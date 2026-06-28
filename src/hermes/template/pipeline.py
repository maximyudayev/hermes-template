############
#
# Copyright (c) 2024-2026 Maxim Yudayev and KU Leuven eMedia Lab
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Created 2024-2025 for the KU Leuven AidWear, AidFOG, and RevalExo projects
# by Maxim Yudayev [https://yudayev.com].
#
# ############

from hermes.utils.time_utils import get_time
from hermes.utils.types import LoggingSpec
from hermes.utils.zmq_utils import (
    PORT_BACKEND,
    PORT_FRONTEND,
    PORT_KILL,
    PORT_SYNC_HOST,
)

from hermes.template.data_container import TemplateDataContainer
from hermes.base.nodes.pipeline import Pipeline


class TemplatePipeline(Pipeline):
    """A template for user extension of the Pipeline behavior, consuming external data and generating new data relayed back to the Broker."""

    def __init__(
        self,
        topic: str,
        host_ip: str,
        data_out_spec: dict,
        data_in_specs: list[dict],
        logging_spec: LoggingSpec,
        is_async_generate: bool = False,
        port_pub: str = PORT_BACKEND,
        port_sub: str = PORT_FRONTEND,
        port_sync: str = PORT_SYNC_HOST,
        port_killsig: str = PORT_KILL,
        **_
    ):
        # TODO: extend the function argument footprint to user-specific function.
        """Constructor of the TemplatePipeline Node.

        Args:
            host_ip (str): IP address of the local master Broker.
            data_out_spec (dict): Mapping of corresponding `DataContainer` object parameters to user-defined configuration values.
            data_in_specs (list[dict]): List of mappings of user-configured incoming modalities.
            logging_spec (LoggingSpec): Mapping of Storage object parameters to user-defined configuration values.
            is_async_generate (bool, optional): Whether the Pipeline produces data asynchronously, in parallel to what is fed into it. Defaults to `False`.
            port_pub (str, optional): Local port to publish to for local master Broker to relay. Defaults to `PORT_BACKEND`.
            port_sub (str, optional): Local port to subscribe to for incoming relayed data from the local master Broker. Defaults to `PORT_FRONTEND`.
            port_sync (str, optional): Local port to listen to for local master Broker's startup coordination. Defaults to `PORT_SYNC_HOST`.
            port_killsig (str, optional): Local port to listen to for local master Broker's termination signal. Defaults to `PORT_KILL`.
        """

        super().__init__(
            topic=topic,
            host_ip=host_ip,
            data_out_spec=data_out_spec,
            data_in_specs=data_in_specs,
            logging_spec=logging_spec,
            is_async_generate=is_async_generate,
            port_pub=port_pub,
            port_sub=port_sub,
            port_sync=port_sync,
            port_killsig=port_killsig,
        )

    @classmethod
    def create_data_container(cls, data_spec: dict) -> TemplateDataContainer:
        return TemplateDataContainer(**data_spec)

    def _keep_samples(self) -> None:
        pass

    def _process_data(self, topic: str, msg: dict) -> None:
        if self._is_continue_produce:
            ###################################
            # TODO: processing results of data.
            ###################################
            process_time_s: float = get_time()
            ###################################
            ###################################

            tag: str = "%s.data" % self.topic
            # TODO: match data keys to device and substream names of the Stream object.
            self._publish(tag, time_s=process_time_s, data=process_time_s)
        else:
            self._send_end_packet()

    def _generate_data(self) -> None:
        pass

    def _stop_new_data(self):
        # TODO: trigger the sensor's backend to stop generating new data.
        pass

    def _cleanup(self) -> None:
        # TODO: perform component-specific clean-up.
        super()._cleanup()
