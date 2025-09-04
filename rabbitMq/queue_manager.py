from connection import create_connection

def create_queues(user_id):
    """Create dynamic queues for a given user_id."""
    try:
        connection = create_connection()
        channel = connection.channel()

        data_queue = f"{user_id}_data"
        command_queue = f"{user_id}_command"

        channel.queue_declare(queue=data_queue, durable=True)
        channel.queue_declare(queue=command_queue, durable=True)

        return True, f"Created queues: {data_queue} and {command_queue}"

    except Exception as e:
        return False, f"Error creating queues: {str(e)}"
    finally:
        connection.close()